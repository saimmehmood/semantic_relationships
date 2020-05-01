 
 -- cell_poi contains cell ids and poi ids for the POIs that are inside cell coordinates.
 
 select c.cell_id, p.poi_enum into table cell_poi
   from poi p, cells c
   where st_within(p.geom_point, c.coordinates) and grid_id = 1225
   order by c.cell_id