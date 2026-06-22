import os
from datetime import datetime



class CaptureScrenshot:
    @staticmethod
    def capture_screenshot(driver, test_case_name):
        # Current Date And Time
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        # Screenshot folder
        screenshot_folder = "screenshot"
        # Create Folder If Not Exists
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        # Screenshot File Name
        screenshot_name = (f"{test_case_name}_{timestamp}.png")
        # Full Path
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        # Save Screenshot
        driver.save_screenshot(screenshot_path)
        return screenshot_path
