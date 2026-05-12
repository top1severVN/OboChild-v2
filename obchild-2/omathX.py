import numpy as np

class mathes:
    """Extended math utilities based on numpy."""

    def add(a, b):
        """Add two values or arrays."""
        return np.add(a, b)

    def sub(a, b):
        """Subtract b from a."""
        return np.subtract(a, b)

    def mul(a, b):
        """Multiply two values or arrays."""
        return np.multiply(a, b)

    def div(a, b):
        """Divide a by b."""
        return np.divide(a, b)

    def powx(a, x):
        """Raise a to the power x."""
        return np.power(a, x)

    def sumx(a):
        """Sum elements of an array."""
        return np.sum(a)

    def minx(a):
        """Return minimum element."""
        return np.min(a)

    def maxx(a):
        """Return maximum element."""
        return np.max(a)

    def absx(a):
        """Return absolute value."""
        return np.abs(a)

    def sqert(a):
        """Return square root."""
        return np.sqrt(a)

    def medi(a):
        """Return mean value."""
        return np.mean(a)

    def stdx(a):
        """Return standard deviation."""
        return np.std(a)

    def varx(a):
        """Return variance."""
        return np.var(a)

    def roundx(a, decimals=0):
        """Round a number or array to the given decimals."""
        return np.round(a, decimals)

    def floorx(a):
        """Return floor of the input."""
        return np.floor(a)

    def ceilx(a):
        """Return ceiling of the input."""
        return np.ceil(a)

    def expx(a):
        """Return e to the power of a."""
        return np.exp(a)

    def logx(a):
        """Return natural logarithm of a."""
        return np.log(a)

    def log2x(a):
        """Return base-2 logarithm of a."""
        return np.log2(a)

    def log10x(a):
        """Return base-10 logarithm of a."""
        return np.log10(a)

    def log1px(a):
        """Return log(1 + a)."""
        return np.log1p(a)

    def sinx(a):
        """Return sine of a (radians)."""
        return np.sin(a)

    def cosx(a):
        """Return cosine of a (radians)."""
        return np.cos(a)

    def tanx(a):
        """Return tangent of a (radians)."""
        return np.tan(a)

    def dot(a, b):
        """Return dot product of two vectors."""
        return np.dot(a, b)

    def cross(a, b):
        """Return cross product of two 3D vectors."""
        return np.cross(a, b)


class vec:
    """Vector helper class for numpy-based operations."""

    def __init__(obj, data=None):
        obj.data = np.array(data) if data is not None else None

    def set(obj, data):
        """Set the vector data from a list or array."""
        obj.data = np.array(data)
        return obj.data

    def show(obj):
        """Return the underlying numpy array."""
        return obj.data

    def dist(obj, other):
        """Return Euclidean distance to another vector."""
        if obj.data is None or other.data is None:
            raise ValueError('Vector data not set')
        return np.linalg.norm(obj.data - other.data)

    def add(obj, other):
        """Add another vector to this vector."""
        obj.data = np.add(obj.data, other.data)
        return obj.data

    def sub(obj, other):
        """Subtract another vector from this vector."""
        obj.data = np.subtract(obj.data, other.data)
        return obj.data

    def scale(obj, scalar):
        """Scale the vector by a scalar."""
        obj.data = np.multiply(obj.data, scalar)
        return obj.data

    def length(obj):
        """Return the vector magnitude."""
        return np.linalg.norm(obj.data)

    def normalize(obj):
        """Normalize the vector to length 1."""
        norm = obj.length()
        if norm == 0:
            return obj.data
        obj.data = obj.data / norm
        return obj.data

    def dot(obj, other):
        """Return dot product with another vector."""
        return np.dot(obj.data, other.data)

    def cross(obj, other):
        """Return cross product with another vector."""
        return np.cross(obj.data, other.data)

    def to_list(obj):
        """Convert vector to a Python list."""
        return obj.data.tolist() if obj.data is not None else None


class matrix:
    """Matrix helper class for common linear algebra operations."""

    def __init__(obj, data=None):
        obj.data = np.array(data) if data is not None else None

    def shape(obj):
        """Return the shape (rows, cols) of the matrix."""
        return obj.data.shape

    def transpose(obj):
        """Return the transposed matrix."""
        return np.transpose(obj.data)

    def dot(obj, other):
        """Multiply matrix by another matrix."""
        return np.dot(obj.data, other.data)

    def det(obj):
        """Return determinant of the matrix."""
        return np.linalg.det(obj.data)

    def inv(obj):
        """Return inverse of the matrix."""
        return np.linalg.inv(obj.data)

    def rank(obj):
        """Return rank of the matrix."""
        return np.linalg.matrix_rank(obj.data)

    def to_list(obj):
        """Convert matrix to a Python nested list."""
        return obj.data.tolist() if obj.data is not None else None

