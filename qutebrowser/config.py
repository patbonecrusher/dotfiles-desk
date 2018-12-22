# From reddit on pywal color integration: 
# https://www.reddit.com/r/qutebrowser/comments/77fkzm/qutebrowser_pywal_is_it_possible_to_use_xrdb_bg/


# ORIGINAL START OF DOCUMENT PRE PYWAL COLOR INTEGRATION BELOW:

# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')




#############################################################
#############################################################
#############################################################
#          CUSTOM STUFF I ADDED BELOW THIS POINT            #
#############################################################
#############################################################
#############################################################


# Change homepage         ((( THIS ATTEMPT FAILED )))

# url.start_pages ["https://pitchfork.com"]



# Enable external blocked hosts list (this adds to the default doesn't replace)

#c.content.host_blocking.lists.append( str(config.configdir) + "/blockedHosts")




######### COLOR THEME SOLUTION BELOW #########

import subprocess
def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props
xresources = read_xresources('*')


###change color for status bar at bottom

c.colors.statusbar.normal.bg = xresources['*background']

###change color for even and odds tabs

c.colors.tabs.even.bg = xresources['*background']
c.colors.tabs.odd.bg = xresources['*background']

######### COLOR THEME SOLUTION ABOVE #########



######### FAILED ATTEMPT AT AUTOMATING COLOR THEME , WENT WITH OTHER SOLUTION #########

#import yaml
#with (config.configdir / 'colors.yml').open() as f:
#yaml_data = yaml.load(f)
#def dict_attrs(obj, path=''):
#if isinstance(obj, dict):
#for k, v in obj.items():
#yield from dict_attrs(v, '{}.{}'.format(path, k) if path else k)
#else:
#yield path, obj
#for k, v in dict_attrs(yaml_data):
#config.set(k, v)

