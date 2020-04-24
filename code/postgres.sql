-- Adding traj table into PostgreSQL to store traj data-sets
create table traj (
  	traj_id serial primary key,  
 	traj_path geometry -- must be LINESTRING type
  )

-- where st_setrid is Spatial Reference System Identifier
update traj set traj_path = st_setsrid(traj_path, 4326) 

-- Adding geographical area grid cells coordinates.
create table cells (
	cell_id serial primary key,  -- changed to serial in cell_01
	grid_id float references grids(grid_id),
	cell_names text,
	coordinates geometry  -- must be POLYGON geometry: need to specify first and last coordinate same for each of them. 
)

-- Converting trajectories from set of geospatial coordinates into
-- set of grid cells.

WITH t1 AS (
  SELECT tr.traj_id, ce.cell_id,
  ST_LineLocatePoint(
      tr.traj_path,
      ST_CENTROID(
          (ST_DUMP(
              ST_Intersection(ce.coordinates, tr.traj_path)
          )).geom
      )
  ) AS distance
  FROM cells ce, traj tr

),

t2 AS (
  SELECT t1.traj_id, t1.cell_id,
  COALESCE(LEAD(t1.cell_id) OVER(ORDER BY t1.traj_id, t1.distance), -1) AS next_cell_id
  FROM t1
)

SELECT t2.traj_id, t2.cell_id into table traj_as_cells
FROM t2
WHERE t2.cell_id <> t2.next_cell_id
;



 