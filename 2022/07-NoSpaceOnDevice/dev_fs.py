from enum import Enum, auto

class FSObj_Type(Enum):
    DIRECTORY = auto()
    FILE = auto()

class DeviceFS():
    FS_Objects = list()

    @classmethod
    def update_fs_objects(cls, fs_obj) -> None:
        cls.FS_Objects.append(fs_obj)

    @classmethod
    def _make_root_dir(cls, caller: str):
        """
        This class method can only be called once and only from the __init__ method.
        After is the "root directory" is created this method is deleted from the class
        to prevent another instance of the root directory from being instantiated.
        """
        #if len(cls.FS_Objects) == 0:
        if caller == 'DeviceFS.__init__':
            """
            fs_objects_idx for '/' will always be 0, because it is the first FS Object to be created.
            Also setting the parent_idx for 0 and the parent = self.  For '/' it is essentially its 
            own parent - Predestination (Ethan Hawke movie)
            """
            fs_objects_idx = 0
            root_dir = Directory(None, '/', fs_objects_idx, 0)
            root_dir.parent = root_dir
            cls.update_fs_objects(root_dir)
            return root_dir

        return cls.FS_Objects[0]

    @classmethod
    def get_root_dir(cls):
        return cls.FS_Objects[0]

    def __init__(self) -> None:
        if len(DeviceFS.FS_Objects) == 0:
            root_dir = DeviceFS._make_root_dir(self.__init__.__qualname__)
            del DeviceFS._make_root_dir

        
class Directory(DeviceFS):
    type: FSObj_Type = FSObj_Type.DIRECTORY

    def update_size(self) -> None:
        if len(self.children) > 0:
            children_size: int = 0
            for child in self.children:
                children_size += child.size
                #print(f'------ Children Information: {child.path}\t{child.size}')
            self.size = children_size
            #if self.parent is not None: self.parent.update_size()
            if self.parent is not self: self.parent.update_size()
        #print(f'--------- Dir size update: {self.path}\t{self.size}')

    def add_child_object(self, type: FSObj_Type, name: str, size: int = 0):
        #print(f'CREATING: {type} = {name} [{size}]')
        f_idx = len(DeviceFS.FS_Objects)
        c_idx = len(self.children)

        fs_obj = Directory(self, name, f_idx, c_idx) if type == FSObj_Type.DIRECTORY else File(self, name, size, f_idx, c_idx)
        
        DeviceFS.update_fs_objects(fs_obj)
        self.children.append(fs_obj)
        self.update_size()

    def get_child_index(self, name: str) -> int:
        for idx, child in enumerate(self.children):
            if name == child.name: return idx

    """
    Change directory function
    """
    def cd(self, name: str):
        """
        This does not handle the case when at the '/' level and running cd ..
        """
        #print(f'Changing Directory to: {name}')
        if name == '/': return self.get_root_dir()

        return self.parent if name == '..' else self.children[self.get_child_index(name)]

    def ls(self) -> None:
        type = '<File>' if self.type == FSObj_Type.FILE else '<Directory>'
        print(f'ls: {self.name}')
        print(f'   {self.path}\t{type}\t{self.size}')
        print(f'     Children:')
        if len(self.children) == 0:
            print(f'        NONE')
        else:
            for child in self.children:
                type = '<File>' if child.type == FSObj_Type.FILE else '<Directory>'
                print(f'        {child.path}\t{type}\t{child.size}')
            print('\n\n')

    
    def __init__(self, parent, name: str, fs_objects_idx: int, parent_idx: int) -> None:
        #super().__init__()
        self.parent: Directory|None = parent
        self.parent_idx: int = parent_idx
        self.fs_objects_idx: int = fs_objects_idx
        self.name: str = name
        self.size: int = 0
        self.children = list()
        self.path: str = '/' if name == '/' else self.parent.path + '/' + name

        if self.path.startswith('//'): self.path = ''.join(list(self.path)[1::])

class File(DeviceFS):
    type: FSObj_Type = FSObj_Type.FILE

    def update_size(self, size: int) -> None:
        self.size += size
        #print(f'--- File size update: {self.path}\t{self.size}')
        self.parent.update_size()

    def __init__(self, parent: Directory, name: str, size: int, fs_objects_idx: int, parent_idx: int) -> None:
        #super().__init__()
        self.parent: Directory = parent
        self.parent_idx: int = parent_idx
        self.fs_objects_idx: int = fs_objects_idx
        self.name: str = name
        self.size: int = 0
        self.path: str = self.parent.path + '/' + name
        
        self.update_size(size)



### Call Main ###
if __name__ == '__main__':
    print('\nImport this file as a module\n')