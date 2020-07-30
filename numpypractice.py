import numpy as np

# =============================================================================
# data = [6,7.5,0,1,0.9,-1]
# arr1 = np.array(data)
# print(arr1)
# print(arr1.dtype)
# =============================================================================

# =============================================================================
# data = [[1,2,3],[9,8,7]]
# arr1 = np.array(data)
# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.dtype)
# =============================================================================

# =============================================================================
# print(np.zeros(10))
# print(np.zeros((3,4)))
# print(np.empty(5))
# print(np.empty((5,2)))
# print(np.empty((5,2,2)))
# print(np.empty((5,1,2)))
# print(np.empty((5,4)))
# =============================================================================
 
# =============================================================================
# print(np.arange(5))
# arr1 = np.array([1, 2, 3], dtype=np.float64)
# print(arr1)
# print(arr1.dtype)
# arr2 = np.array([1, 2, 3], dtype=np.int32)
# print(arr2)
# print(arr2.dtype)
# =============================================================================

# =============================================================================
# '''convert data type of an array to another array.'''
# '''numpy decides datatype based on data given'''
# arr = np.array([1, 2, 3, 4, 5])
# print(arr.dtype)
# float_arr = arr.astype(np.float64)
# print(float_arr)
# print(float_arr.dtype)
# arr = np.array([1.2, -2.1, 3.6, 4.2, 5.8])
# print(arr.dtype)
# int_arr = arr.astype(np.int64)
# print(int_arr)
# print(int_arr.dtype)
# arr = np.array(['1.2', '-2.1', '3.6', '4.2', '5.8'], dtype=np.string_)
# print(arr.dtype)
# int_arr = arr.astype(np.float)
# print(int_arr)
# print(int_arr.dtype)
# int_array = np.arange(10)
# some_flt_array = np.array([.22,1.2,3.4,9.8], dtype=np.float64)
# print(int_array.astype(some_flt_array.dtype))
# =============================================================================

# =============================================================================
# ''' scalar operations on Numpy arrays '''
# arr = np.array([[1,2,3],[1,2,3]])
# print(arr*arr)
# print(2*arr)
# print(1/arr)
# print(arr**.5)
# =============================================================================

# =============================================================================
# ''' Numpy array slicing '''
# arr = np.arange(10)
# print(arr)
# arr1 =  arr[5:8]
# print(arr1)
# arr[5:8] = 1
# print(arr)
# =============================================================================

# =============================================================================
# '''Multi dimensional array operations using Numpy'''
# arr2d = np.array([[1,2],[3,4]])
# print(arr2d)
# arr3d = np.array([[[1,2,3],[4,5,6]],[[1,1,1],[2,2,2]]])
# print(arr3d)
# print(arr3d[0])
# old_values = arr3d[0].copy()
# arr3d[0] = 1
# print(arr3d)
# arr3d[0] = old_values
# print(arr3d)
# arr2d = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# print(arr2d)
# arr4d = np.array([[[[1,2,3],[4,5,6]],[[1,1,1],[2,2,2]]],[[[1,2,3],[4,5,6]],
#                                                          [[1,1,1],[2,2,2]]]])
# print(arr4d)
# arr3d = np.array([[[1,2,3],[4,5,6]],[[1,1,1],[2,2,2]]])
# print(arr3d[1,1])
# print(arr3d[1])
# arr2d = np.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]])
# print(arr2d[:1])
# =============================================================================

