import pymeshlab
import webbrowser
import paramiko

command='cd /home/user_236/project/ICON; /home/user_236/miniconda3/envs/icon/bin/python  -m apps.infer -cfg ' \
        './configs/icon-filter.yaml -gpu 0 -in_dir ./input -out_dir ./output -export_video -loop_smpl 100  ' \
        '-loop_cloth 200 -hps_type pymaf '

print("open connection")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('control36.ef.technion.ac.il', username='user_236', password='Nadav@Yotam')

stdin, stdout, stderr = ssh.exec_command('cd /home/user_236/project/ICON; mkdir output;  mkdir input')



ftp_client=ssh.open_sftp()
ftp_client.put('../input/input_yotam.jpeg', '/home/user_236/project/ICON/input/input_yotam.jpeg')
ftp_client.close()

stdin, stdout, stderr = ssh.exec_command(command)

for line in stdout:
    print(line.rstrip())

found_err = False
for line in stderr:
    found_err = True
    print(line.rstrip())
if found_err:
    print("errorroror!!!!!!!")
    exit(1)

ftp_client = ssh.open_sftp()
ftp_client.get('cd /home/user_236/project/ICON/output/input_yotam.obj', 'output/input_yotam.obj',)
ftp_client.close()
ssh.close()
# create a new MeshSet
ms = pymeshlab.MeshSet()

# load mesh
ms.load_new_mesh("output_yotam.obj")

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

