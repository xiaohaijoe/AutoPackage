import subprocess

class ProcessInstance:

    __instance = None
    cwd = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @classmethod
    def run(cls, command):
        p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cls.cwd)
        out, err = p.communicate()
        out = bytes.decode(out)
        err = bytes.decode(err)
        res = ""
        if out != "":
            return True, out
        elif err.startswith("fatal"):
            return False, err
        else:
            return True, err

    @classmethod
    def setCwd(cls, cwd):
        cls.cwd = cwd

    @classmethod
    def clear(cls):
        cls.cwd = None
