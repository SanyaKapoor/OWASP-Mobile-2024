import os
import re
import subprocess

def decompile_apk(apk_file_path, output_directory):
    # Create a new directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    subprocess.run(["java", "-jar", "C:/Windows/apktool.jar", "d", apk_file_path, "-o", output_directory, "-f"])

    # Run apktool to decompile the APK
    #subprocess.run(["C:/Windows/apktool.jar", "d", apk_file_path, "-o", output_directory, "-f"])

def check_verification_metadata(output_directory):
    # Check if verification-metadata.xml file is present in the decompiled code
    verification_metadata_path = os.path.join(output_directory, "res/xml/verification-metadata.xml")
    return os.path.exists(verification_metadata_path)

def check_trusted_keys(output_directory):
    # Check if <trusted-keys> is present in the verification-metadata.xml file
    verification_metadata_path = os.path.join(output_directory, "res/xml/verification-metadata.xml")
    if os.path.exists(verification_metadata_path):
        with open(verification_metadata_path, "r") as f:
            content = f.read()
            return "<trusted-keys>" in content
    else:
        return False

# def check_common_passwords(output_directory):
#     common_passwords_regex = re.compile(r"(123456|password|123456789|12345678|12345|1234567|admin|123123|qwerty|abc123|letmein|monkey|111111|password1|qwerty123|dragon|1234|baseball|iloveyou|trustno1|sunshine|princess|football|welcome|shadow|superman|michael|ninja|mustang|jessica|charlie|ashley|bailey|passw0rd|master|love|hello|freedom|whatever|nicole|jordan|cameron|secret|summer|1q2w3e4r|zxcvbnm|starwars|computer|taylor|startrek)")
#     for root, dirs, files in os.walk(output_directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 with open(file_path, "r", encoding="utf-8") as f:  # Specify the encoding
#                     content = f.read()
#                     if common_passwords_regex.search(content):
#                         return True
#     return False

def check_des_usage(output_directory):
    # Check if DES is used in the code
    des_usage_regex = re.compile(r"(?!.*\b(?!SecretKeySpec\b)(?!DES\b).*)")
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, "r") as f:
                    content = f.read()
                    if des_usage_regex.search(content):
                        return True
    return False

def main():
    # Path to the APK file
    apk_file_path = "diva.apk"
    output_directory = "C:\\Users\\002DNA744\\Downloads\\Data"

    # Decompile the APK
    decompile_apk(apk_file_path, output_directory)

    # Check if verification-metadata.xml is present
    if check_verification_metadata(output_directory):
        print("verification-metadata.xml is present in the decompiled code.")
    else:
        print("verification-metadata.xml is not present in the decompiled code.")

    # Check if <trusted-keys> is present
    if check_trusted_keys(output_directory):
        print("<trusted-keys> is present in the verification-metadata.xml file.")
    else:
        print("<trusted-keys> is not present in the verification-metadata.xml file.")

    # Check if any hardcoded common passwords are present
    # if check_common_passwords(output_directory):
    #     print("Common passwords are present in the decompiled code.")
    # else:
    #     print("No common passwords are present in the decompiled code.")

    # Check if DES is used
    if check_des_usage(output_directory):
        print("DES encryption algorithm is used in the decompiled code.")
    else:
        print("DES encryption algorithm is not used in the decompiled code.")

if __name__ == "__main__":
    main()