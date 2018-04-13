## *********************************************************
## 
## File autogenerated for the softkinetic_camera package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 293, 'description': 'Camera optical frame', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'camera_link', 'edit_method': '', 'default': 'base_rgbd_camera_optical_frame', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Confidence threshold', 'max': 2000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'confidence_threshold', 'edit_method': '', 'default': 200, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 293, 'description': 'Enable downsampling (voxel grid) filter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_voxel_grid_filter', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Voxel grid size', 'max': 0.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'voxel_grid_size', 'edit_method': '', 'default': 0.01, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Enable radius outlier removal filter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_radius_outlier_filter', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Search radius', 'max': 0.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'search_radius', 'edit_method': '', 'default': 0.05, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Minimum number of neightbours within the search radius', 'max': 500, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_neighbours', 'edit_method': '', 'default': 50, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 293, 'description': 'Enable passthrough filter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_passthrough_filter', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Limit minimum value', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'limit_min', 'edit_method': '', 'default': 0.01, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Limit maximum value', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'limit_max', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Enable frustum culling filter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_frustum_culling_filter', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Horizontal FOV (degrees)', 'max': 180.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'hfov', 'edit_method': '', 'default': 90.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Vertical FOV (degrees)', 'max': 180.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vfov', 'edit_method': '', 'default': 90.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Near plane', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'near_plane', 'edit_method': '', 'default': 0.01, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Far plane', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'far_plane', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'Enable serial number identification', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_serial', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Camera serial number', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'serial', 'edit_method': '', 'default': '', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Enable depth', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enable_depth', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Depth mode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_mode', 'edit_method': "{'enum_description': 'Depth modes', 'enum': [{'srcline': 40, 'description': 'Close mode', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'close', 'ctype': 'std::string', 'type': 'str', 'name': 'close'}, {'srcline': 41, 'description': 'Long mode', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'long', 'ctype': 'std::string', 'type': 'str', 'name': 'long'}]}", 'default': 'close', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Depth frame format', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_frame_format', 'edit_method': "{'enum_description': 'Depth frame formats', 'enum': [{'srcline': 44, 'description': 'QQVGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'QQVGA', 'ctype': 'std::string', 'type': 'str', 'name': 'QQVGA'}, {'srcline': 45, 'description': 'QVGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'QVGA', 'ctype': 'std::string', 'type': 'str', 'name': 'QVGA'}, {'srcline': 46, 'description': 'VGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'VGA', 'ctype': 'std::string', 'type': 'str', 'name': 'VGA'}]}", 'default': 'QQVGA', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Depth frame rate', 'max': 60, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_frame_rate', 'edit_method': "{'enum_description': 'Depth frame rates', 'enum': [{'srcline': 51, 'description': '25Hz', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const int', 'value': 25, 'ctype': 'int', 'type': 'int', 'name': '25'}, {'srcline': 52, 'description': '30Hz', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const int', 'value': 30, 'ctype': 'int', 'type': 'int', 'name': '30'}, {'srcline': 53, 'description': '50Hz', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const int', 'value': 50, 'ctype': 'int', 'type': 'int', 'name': '50'}, {'srcline': 54, 'description': '60Hz', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const int', 'value': 60, 'ctype': 'int', 'type': 'int', 'name': '60'}]}", 'default': 30, 'level': 0, 'min': 25, 'type': 'int'}, {'srcline': 293, 'description': 'Enable color', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enable_color', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'Color compression', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_compression', 'edit_method': "{'enum_description': 'Color compressions', 'enum': [{'srcline': 57, 'description': 'YUY2', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'YUY2', 'ctype': 'std::string', 'type': 'str', 'name': 'YUY2'}, {'srcline': 58, 'description': 'MJPEG', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'MJPEG', 'ctype': 'std::string', 'type': 'str', 'name': 'MJPEG'}]}", 'default': 'MJPEG', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Color frame format', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_frame_format', 'edit_method': "{'enum_description': 'Color frame formats', 'enum': [{'srcline': 44, 'description': 'QQVGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'QQVGA', 'ctype': 'std::string', 'type': 'str', 'name': 'QQVGA'}, {'srcline': 45, 'description': 'QVGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'QVGA', 'ctype': 'std::string', 'type': 'str', 'name': 'QVGA'}, {'srcline': 46, 'description': 'VGA', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'VGA', 'ctype': 'std::string', 'type': 'str', 'name': 'VGA'}, {'srcline': 47, 'description': 'NHD', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'NHD', 'ctype': 'std::string', 'type': 'str', 'name': 'NHD'}, {'srcline': 48, 'description': 'WXGA_H', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const char * const', 'value': 'WXGA_H', 'ctype': 'std::string', 'type': 'str', 'name': 'WXGA_H'}]}", 'default': 'VGA', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'Color frame rate', 'max': 30, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_frame_rate', 'edit_method': "{'enum_description': 'Color frame rates', 'enum': [{'srcline': 52, 'description': '30Hz', 'srcfile': '/home/sapta/ws/src/softkinetic/softkinetic_camera/cfg/Softkinetic.cfg', 'cconsttype': 'const int', 'value': 30, 'ctype': 'int', 'type': 'int', 'name': '30'}]}", 'default': 30, 'level': 0, 'min': 30, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Softkinetic_close = 'close'
Softkinetic_long = 'long'
Softkinetic_QQVGA = 'QQVGA'
Softkinetic_QVGA = 'QVGA'
Softkinetic_VGA = 'VGA'
Softkinetic_NHD = 'NHD'
Softkinetic_WXGA_H = 'WXGA_H'
Softkinetic_25 = 25
Softkinetic_30 = 30
Softkinetic_50 = 50
Softkinetic_60 = 60
Softkinetic_YUY2 = 'YUY2'
Softkinetic_MJPEG = 'MJPEG'
