from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas
from compas.geometry import Vector
from compas_rhino.geometry.point import RhinoPoint

if compas.RHINO:
    import Rhino


__all__ = ['RhinoVector']


class RhinoVector(RhinoPoint):
    """Wrapper for a Rhino vector objects."""

    def __init__(self):
        super(RhinoVector, self).__init__()

    @classmethod
    def from_geometry(cls, geometry):
        """Construct a vector wrapper from an existing geometry object.

        Parameters
        ----------
        geometry : vector or :class:`Rhino.Geometry.Point3d` or :class:`Rhino.Geometry.Vector3d`
            The input geometry.

        Returns
        -------
        :class:`compas_rhino.geometry.RhinoVector`
            The wrapped vector.
        """
        if not isinstance(geometry, (Rhino.Geometry.Vector3d, Rhino.Geometry.Point3d)):
            geometry = Rhino.Geometry.Vector3d(geometry[0], geometry[1], geometry[2])
        vector = cls()
        vector.geometry = geometry
        return vector

    @classmethod
    def from_selection(cls):
        raise NotImplementedError

    def to_compas(self):
        """Convert the wrapper to a COMPAS object.

        Returns
        -------
        :class:`compas.geometry.Vector`
            The COMPAS vector.
        """
        return Vector(self.x, self.y, self.z)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
