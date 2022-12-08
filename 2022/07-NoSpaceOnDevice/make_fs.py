import sys

import dev_fs as dfs

def command(fsobj: dfs.Directory, cmd) -> dfs.Directory:
    if cmd[0] == 'cd':
        #fsobj = fsobj.cd(cmd[1])
        #print(f'\nCmd = {cmd}\n')
        return fsobj.cd(cmd[1])

    if cmd[0] == 'ls':
        fsobj.ls()
        return fsobj

def make_fs(fsobj: dfs.Directory, t_out) -> None:
    for i, line in enumerate(t_out, start=1):
        #if i > 5: break
        #print(f'Line {i}   : {line}')
        line = str(line)
        
        if line.startswith('$'):
            _, *cmd = line.split()
            fsobj = command(fsobj, cmd)
            #print(f'FSOBJ = {fsobj.name}  Parent Name = tmpfsobj.parent.name')
        else:
            attribute, name = line.split()
        
            if attribute == 'dir':
                fsobj.add_child_object(dfs.FSObj_Type.DIRECTORY, name, 0)
            else:
                fsobj.add_child_object(dfs.FSObj_Type.FILE, name, int(attribute))
        
        #fsobj.ls()

def cleanup_fs(max_capacity: int, min_free_reqd: int) -> dfs.Directory:
    space_used: int = dfs.DeviceFS.FS_Objects[0].size
    space_available: int = max_capacity - space_used

    if space_available >= min_free_reqd: return None

    min_to_free = min_free_reqd - space_available

    cleanup_dirs = list()

    for dir in [dir_objs for dir_objs in dfs.DeviceFS.FS_Objects if dir_objs.type == dfs.FSObj_Type.DIRECTORY]:
        if dir.size < min_to_free: continue
        cleanup_dirs.append(dir)
    
    cleanup_dirs = sorted(cleanup_dirs, key=lambda dir: dir.size)

    #print('\n\nCLEANUP\n\n')
    #for dir in cleanup_dirs:
    #    print(f'{dir.path}   <{dir.type}>\t\t{dir.size}')
    return cleanup_dirs[0]

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    terminal_output = list()

    with open(sys.argv[1]) as f:
        for line in f:
            terminal_output.append(line.strip('/'))
        
    device_fs: dfs.Directory = dfs.DeviceFS().get_root_dir()
    make_fs(device_fs, terminal_output)
    device_fs.ls()

    dir_size: int = 0
    file_size: int = 0

    for i, fsobj in enumerate(dfs.DeviceFS.FS_Objects, start=1):
        if fsobj.type == dfs.FSObj_Type.DIRECTORY and fsobj.size <= 100000:
            #print(f'--- Calculating Total Dir Size: {fsobj.path} [{fsobj.size}]')
            dir_size += fsobj.size
            print(f'{fsobj.name}\t\tSize = {fsobj.size}\t\t{fsobj.path}')
        if fsobj.type == dfs.FSObj_Type.FILE: file_size += fsobj.size
        #print(f'{fsobj.path}\t{fsobj.size}\t{fsobj.type}')
    
    print(f'\n\nDirectory Size = {dir_size}\nFile Size = {file_size}\n\n\n')

    device_fs_max_capacity: int = 70000000
    device_fs_min_free_capacity = 30000000

    dir_cleanup: dfs.Directory = cleanup_fs(device_fs_max_capacity, device_fs_min_free_capacity)

    print(f'Cleanup Recommendation:  {dir_cleanup.path}\t{dir_cleanup.size}')
    dir_cleanup.ls()

    

### Call Main ###
if __name__ == '__main__':
    main()