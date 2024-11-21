import asyncio
import os
from dotenv import load_dotenv

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.services.mlmodel import MLModelClient
from viam.services.vision import VisionClient

load_dotenv()
API_KEY=os.getenv('VIAM_API_KEY_VALUE')
API_KEY_ID=os.getenv('VIAM_API_KEY_ID')
ROBOT_ADDRESS = 'viamvision-main.ei59t0va5a.viam.cloud'

async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key=API_KEY,
        api_key_id=API_KEY_ID
    )
    return await RobotClient.at_address(ROBOT_ADDRESS, opts)

async def person_detect():
    """
    Detects the presence of a person in an image using a VIAM machine's Vision services.

    This function connects to a VIAM cloud-hosted robot client, captures an image using
    the specified camera, and uses an image classification service to analyze the image 
    for the presence of a person. It evaluates detections with a confidence threshold 
    of 80%.

    Returns:
        int: 1 if a person is detected with at least 80% confidence, 0 otherwise.
    """
    # Connect to VIAM machine
    machine = await connect()
    # create a camera obj from Macbook-Pro
    macbook_pro = Camera.from_robot(machine, "Macbook-Pro")
    # create an image classifier object
    img_classify = VisionClient.from_robot(machine, "img_classify")
    # take a snapshot
    img = await macbook_pro.get_image(mime_type="image/jpeg")
    # classify image contents 
    img_contents = await img_classify.get_detections(img)
    # scan thru contents to check for person with high certainty
    for item in img_contents:
        if item.confidence > 0.8 and item.class_name.lower() == 'person':
            await machine.close()
            return 1
    await machine.close()
    return 0

if __name__ == '__main__':
    print(asyncio.run(person_detect()))

