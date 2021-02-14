# import compas_blender
import bpy  # TODO this should not be done here... call utility-functions from this artist instead
from ._shapeartist import ShapeArtist
import compas_blender


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

        compas_blender.clear_collection("BoxArtist")  # TODO properly nest collection creation

        for point in pcl.points:
            box = tpl.copy()
            box.frame.point = point
            artist = BoxArtist(box, color=i_to_rgb(random.random()), collection="BoxArtist")
            artist.draw()
    """

    def draw(self, alpha = 1.0):
        """Draw the box associated with the artist.

        Parameters
        ----------
        alpha: float
            opacity of the object that will be created
        Returns
        -------
        list
            List of blender objects
        """
        # https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add

        if self.collection and self.collection not in bpy.data.collections.keys():
            compas_blender.utilities.create_collection(self.collection)

        box_location = self.shape.frame.point
        box_rotation = self.shape.frame.axis_angle_vector.data
        box_dimensions = (self.shape.xsize,
                          self.shape.ysize,
                          self.shape.zsize)
        bpy.ops.mesh.primitive_cube_add(
            location=box_location,
            rotation=box_rotation,
            scale=box_dimensions)

        created_box = bpy.context.active_object
        compas_blender.utilities.drawing._set_object_color(created_box, self.color, alpha)  # TODO: is it smart to use private func here?
        compas_blender.utilities.drawing._link_object(created_box, self.collection)

        # testing compas_blender.draw_cubes()
        # box_dimensions = Vector.from_data(box_dimensions)  # doesnt work: draw_cubes needs a bpy.Vector not compas.Vector
        # cubedict = {"pos":box_location, "size":3, "color":self.color}
        # compas_blender.draw_cubes([cubedict])

        return [ created_box ]


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    pass
