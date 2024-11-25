import unittest
from goespatial_processing import calculate_raster_statistics

class TestGeospatialProcessing(unittest.TestCase):
    def test_calculate_raster_statistics_real_raster(self):
        # Path to the raster file
        raster_path = '/Users/rodrigo/Desktop/raster_library_example/out_test.tif'
        
        # Call the function and calculate statistics
        stats = calculate_raster_statistics(raster_path)
        
        # Expected values (modify these based on the raster content)
        expected_mean = 655.5116179845223  # Replace with the actual mean you expect
        expected_min = -129      # Replace with the actual minimum
        expected_max = 3106    # Replace with the actual maximum
        
        # Assertions to validate the output
        self.assertAlmostEqual(stats['mean'], expected_mean, places=1)
        self.assertEqual(stats['min'], expected_min)
        self.assertEqual(stats['max'], expected_max)
