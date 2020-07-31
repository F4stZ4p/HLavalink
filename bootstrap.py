"""
Lavalink on Heroku bootstrap script
Credit to diniboy for sed script
"""

from os import system, environ, popen


class LavalinkBootstrap:

    """
    Class we're using to get Lavalink working on Heroku
    """
    
    def prepare_version_number(self):
        
        self._version_number = popen(
            
            """curl --silent "https://api.github.com/repos/Frederikam/Lavalink/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")'"""
          
        ).read().strip()

    def __init__(self):

        """
        Doing important stuff here
        """
        
        self.prepare_version_number() # Fixes #1
        
        self.use_dev_lavalink = True if str(environ.get("USE_DEV_LAVALINK")).lower() not in ("no", "0", "n") else False
        if self.use_dev_lavalink:
            
            print("[INFO] Using developer Lavalink version")
        
        self.download_command = f"curl -L https://ci.fredboat.com/repository/download/Lavalink_Build/8231:id/Lavalink.jar?guest=1 -o Lavalink.jar" if self.use_dev_lavalink else f"curl -L https://github.com/Frederikam/Lavalink/releases/download/{self._version_number}/Lavalink.jar -O"
        print(f"[INFO] Download command: {self.download_command}")
        
        self.replace_port_command = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'

        self.replace_password_command = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.replace_password_command_no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
        
        self._additional_options = environ.get(
            "ADDITIONAL_JAVA_OPTIONS"
        ) # Heroku provides basic Java configuration based on dyno size, no need in limiting memory
    
        self.run_command = f"java -jar Lavalink.jar {self._additional_options}" # User-provided config, will override heroku's

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

    LavalinkBootstrap().run()
