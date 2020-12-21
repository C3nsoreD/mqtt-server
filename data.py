import io
from threading import Condition 

"""
    Represents the data object
        Data Object:
            uav_id:
            camera: binary data
            attitude: 
            gps: 
"""



class StreamingObject(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
        # collects the imu data
        # self.position = connection["attitude"]

    def write(self, buf):
        # Find the bimary stream containing the binary image
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()

            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notifyAll()
            self.buffer.seek()

        return self.buffer.write(buf)
     
    def get_id(self):
        return self.uav_id
    
    def to_quaternion(self):
        """
            Converts the euler attitude to quaternion representation
        """
        pass 


class StreamingObject:
    def __init__(self):
        self.frame = None
