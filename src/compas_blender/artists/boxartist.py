# import compas_blender
import bpy  # TODO this should not be done here... call utility-functions from this artist instead
from ._shapeartist import ShapeArtist
import compas_blender
from compas.geometry import Vector

class BoxArtist(ShapeArtist):
    """Artist for drawing box shapes in Blender.

    Parameters
    ----------
    shape : :class:`compas.geometry.Box`
        A COMPAS box.

    Notes
    -----
    See :class:`compas_blender.artists.ShapeArtist` for all other parameters.

    Examples
    --------
    .. code-block:: python

        import random
        from compas.geometry import Pointcloud
        from compas.geometry import Box
        from compas.utilities import i_to_rgb

        import compas_blender
        from compas_blender.artists import BoxArtist

        pcl = Pointcloud.from_bounds(10, 10, 10, 100)
        tpl = Box.from_width_height_depth(0.3, 0.3, 0.3)

        compas_blender.clear_collection("Test::BoxArtist") TODO properly nest collection creation 


        for point in pcl.points:
            box = tpl.copy()
            box.frame.point = point
            artist = BoxArtist(box, color=i_to_rgb(random.random()), layer="Test::BoxArtist")
            artist.draw()
    """

    def draw(self, show_vertices=False, show_edges=False, show_faces=True, join_faces=True):
        """Draw the box associated with the artist.

        Parameters
        ----------
        show_vertices : bool, optional
            Default is ``False``.
        show_edges : bool, optional
            Default is ``False``.
        show_faces : bool, optional
            Default is ``True``.
        join_faces : bool, optional
            Default is ``True``.

        Returns
        -------
        list
            The GUIDs of the objects created in Blender.
        """

        # bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
        # https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add
        print("attempting to draw box")
        box_location = self.shape.frame.point
        box_rotation = self.shape.frame.axis_angle_vector.data
        box_dimensions = (self.shape.xsize,
                          self.shape.ysize,
                          self.shape.zsize)
        box_dimensions = Vector.from_data(box_dimensions)
        # bpy.ops.mesh.primitive_cube_add(
        #     location=box_location,
        #     rotation=box_rotation,
        #     scale=box_dimensions)
        # bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        cubedict = {"pos":box_location, "size":box_dimensions, "color":self.color}
        compas_blender.draw_cubes([cubedict])


        """
        vertices = [list(vertex) for vertex in self.shape.vertices]
        guids = []
        if show_vertices:
            points = [{'pos': point, 'color': self.color, 'name': self.name} for point in vertices]
            guids += compas_blender.draw_points(points, layer=self.layer, clear=False, redraw=False)
        if show_edges:
            edges = self.shape.edges
            lines = [{'start': vertices[i], 'end': vertices[j], 'color': self.color, 'name': self.name} for i, j in edges]
            guids += compas_blender.draw_lines(lines, layer=self.layer, clear=False, redraw=False)
        if show_faces:
            faces = self.shape.faces
            if join_faces:
                guid = compas_blender.draw_mesh(vertices, faces, layer=self.layer, name=self.name, color=self.color, disjoint=True)
                guids.append(guid)
            else:
                polygons = [{'points': [vertices[index] for index in face], 'color': self.color, 'name': self.name} for face in faces]
                guids += compas_blender.draw_faces(polygons, layer=self.layer, clear=False, redraw=False)
        self._guids = guids
        return guids
        """


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    pass
