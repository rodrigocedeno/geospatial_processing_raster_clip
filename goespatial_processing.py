import geopandas as gpd
import rasterio
from rasterio.mask import mask
from shapely.geometry import mapping
import numpy as np

def load_shapefile(shapefile_path):
    """
    Load a shapefile and return a GeoDataFrame.
    """
    shapefile = gpd.read_file(shapefile_path)
    print(shapefile.head())  # Display first few rows
    return shapefile

def load_raster(raster_path):
    """
    Load a raster and return metadata and the first band.
    """
    with rasterio.open(raster_path) as src:
        data = src.read(1)  # First band
        print(f"Raster dimensions: {src.width}x{src.height}")
        return src.meta, data

def clip_raster_with_shapefile(raster_path, shapefile, output_path):
    """
    Clip a raster using a shapefile and save the result.
    """
    with rasterio.open(raster_path) as src:
        shapes = [mapping(geom) for geom in shapefile.geometry]
        out_image, out_transform = mask(src, shapes, crop=True)
        out_meta = src.meta.copy()
        out_meta.update({
            "driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform
        })
        with rasterio.open(output_path, "w", **out_meta) as dest:
            dest.write(out_image)
    print(f"Clipped raster saved to {output_path}")

def calculate_raster_statistics(raster_path):
    """
    Calculate statistics (mean, min, max, std) for a raster.
    """
    with rasterio.open(raster_path) as src:
        data = src.read(1)  # First band
        data = data[data != src.nodata]  # Exclude nodata values
        stats = {
            "mean": np.mean(data),
            "min": np.min(data),
            "max": np.max(data),
            "std": np.std(data)
        }
        print("Raster Statistics:", stats)
        return stats