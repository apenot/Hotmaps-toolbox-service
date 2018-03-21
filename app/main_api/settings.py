# Flask settings
#FLASK_SERVER_NAME = '0.0.0.0:80'
FLASK_SERVER_NAME = '0.0.0.0:5556'
FLASK_DEBUG = False  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
RESTPLUS_JSON = {
    'separators': (',', ':')
}

CORS_HEADER_API_KEY = 'av7e7d78f93e2af'
CORS_ORIGIN = 'http://hotmaps.hevs.ch'
CORS_CREDENTIALS = False
CORS_HEADERS = (
    CORS_HEADER_API_KEY,
    'X-Fields',
    'Content-Type',
    'Accept',
    'Accept-Charset',
    'Accept-Language',
    'Cache-Control',
    'Content-Encoding',
    'Content-Length',
    'Content-Security-Policy',
    'Content-Type',
    'Cookie',
    'ETag',
    'Host',
    'If-Modified-Since',
    'Keep-Alive',
    'Last-Modified',
    'Origin',
    'Referer',
    'User-Agent',
    'X-Forwarded-For',
    'X-Forwarded-Port',
    'X-Forwarded-Proto'
)

# SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Duration curve constants used in heat.load.profile.py
HOURS_PER_YEAR = 8760
LIMIT_VALUES_PER_NUTS = 4000
POINTS_FIRST_GROUP_PERCENTAGE = 0.0228
POINTS_SECOND_GROUP_PERCENTAGE = 0.1141
POINTS_THIRD_GROUP_PERCENTAGE = 0.7207
POINTS_FOURTH_GROUP_PERCENTAGE = 0.1424
POINTS_FIRST_GROUP_STEP = 12
POINTS_SECOND_GROUP_STEP = 40
POINTS_THIRD_GROUP_STEP = 134
POINTS_FOURTH_GROUP_STEP = 39

# heat load and duration curve data options
NUMBER_DECIMAL_DATA = 2

#name of repository
POPULATION_TOT = 'pop_tot_curr_density'
HEAT_DENSITY_TOT = 'heat_tot_curr_density'
HEAT_DENSITY_NON_RES = 'heat_nonres_curr_density'
HEAT_DENSITY_RES = 'heat_res_curr_density'
WWTP = 'wwtp'
GRASS_FLOOR_AREA_TOT = 'gfa_tot_curr_density'
GRASS_FLOOR_AREA_RES = 'gfa_res_curr_density'
GRASS_FLOOR_AREA_NON_RES = 'gfa_nonres_curr_density'
BUILDING_VOLUMES_RES = 'vol_res_curr_density'
BUILDING_VOLUMES_TOT = 'vol_tot_curr_density'
BUILDING_VOLUMES_NON_RES = 'vol_nonres_curr_density'
INDUSTRIAL_SITES = 'industrial_sites_Industrial_Database'
BIOMASS_POTENTIAL = 'potential_biomass'
MUNICIPAL_SOLID_WASTE = 'potential_municipal_solid_waste'
WIND_POTENTIAL = 'potential_wind'
SOLAR_POTENTIAL = 'potential_solar'
GEOTHERMAL_POTENTIAL = 'potential_shallowgeothermal'