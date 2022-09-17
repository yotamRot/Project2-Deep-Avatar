import pymeshlab
import webbrowser
import paramiko


ssh = paramiko.SSHClient()
ssh.connect('control36', username='user_236', password='Nadav@Yotam')
stdin, stdout, stderr = ssh.exec_command('python -u /home/user/test.py')
for line in stdout:
    print(line.rstrip())




# create a new MeshSet
ms = pymeshlab.MeshSet()

# load mesh
ms.load_new_mesh("chinese.obj")

# apply convex hull filter to the current selected mesh (last loaded)
ms.compute_texcoord_parametrization_triangle_trivial_per_wedge() # textname will be filename of a png, should not be a full path

ms.compute_texmap_from_color(textname=f"my_texture_name.jpg") # textname will be filename of a png, should not be a full path


# save the current selected mesh
ms.save_current_mesh("convex_hull.obj")

# get a reference to the current selected mesh
m = ms.current_mesh()

print(m.vertex_number())


url = 'https://www.mixamo.com/#/?type=Motion%2CMotionPack'

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

