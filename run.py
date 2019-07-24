"""
Lavalink on Heroku boostrap script
"""

from os import system, environ

class LavalinkBoostrap:

    """
    Class we're using to get Lavalink working on Heroku
    """

    def __init__(self):

        """
        Doing important stuff here
        """

        self.download_command = "curl -s https://api.github.com/repos/Frederikam/Lavalink/releases/latest | grep browser_download_url | cut -d '\"' -f 4 | wget -qi -"

        self.replace_port_command = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'

        self.replace_password_command = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.replace_password_command_no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
    
        self.run_command = "java -jar Lavalink.jar"

    def replace_password_and_port(self):

        """
        Replacing password and port in application.yml
        """

        print(
            "[INFO] Replacing port..."
        )

        try:
            
            system(
                self.replace_port_command
            )

            if not environ.get("PASSWORD"):

                print(
                    """
                    [WARNING] You have not specified your Lavalink password in config vars. To do this, go to settings 
                    and set the PASSWORD environment variable
                    """
                )
    
                return system(
                    self.replace_password_command_no_password
                )
            
            system(
                self.replace_password_command
            )

        except BaseException as exc:

            print(
                f"[ERROR] Failed to replace port/password. Info: {exc}"
            )

        else:

            print(
                "[INFO] Done. Config is ready now"
            )

    def download(self):

        """
        Downloads latest release of Lavalink
        """

        print(
            "[INFO] Downloading latest release of Lavalink..."
        )
        
        try:
            
            system(
                self.download_command
            )
        
        except BaseException as exc:

            print(
                f"[ERROR] Lavalink download failed. Info: {exc}"
            )

        else:
        
            print(
                "[INFO] Lavalink download OK"
            )
    
    def run(self):

        """
        Runs Lavalink instance
        """

        self.download()
        self.replace_password_and_port()

        print(
            "[INFO] Starting Lavalink..."
        )

        try:

            system(
                self.run_command
            )
        
        except BaseException as exc:

            print(
                f"[ERROR] Failed to start Lavalink. Info: {exc}"
            )

if __name__ == "__main__":

    """
    Starts our instance
    """

    LavalinkBoostrap().run()