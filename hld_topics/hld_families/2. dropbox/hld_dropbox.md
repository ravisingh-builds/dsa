# Dropbox:
        1. It cloud-based file-storage service allows users to store and share files.
        2. It provides a secure and reliable way to store and access files from anywhere, on any device.

# 1. Requirements: 

- Funtional: What is the product suppose to do? Top 3/4 features?
    - **Users can upload a file from any device to remote storage.**
        - Note: Upload means "put this file into Dropbox." You pick a photo on your phone and send it. Remote storage means Dropbox saves that photo on its own computers. Your phone still has the photo too. After that, your laptop and your work computer get the photo from Dropbox. They cannot open it from the phone itself.
    - **Users can download a file onto any device from remote storage.**
        - Note: Download means this device asks Dropbox for a file the cloud already has, and Dropbox copies it onto this device. You took a photo on your phone and uploaded it. Later, on your laptop, you download that photo. The laptop cannot read the phone, so it gets Dropbox's copy.
    - **Users can share a file with other users and view the files shared with them.**
        - Note: Share is for another person. You give a friend access to resume.pdf. Your friend can view it and download Dropbox's copy onto their computer. Your own phone getting that same file is sync, which is the next requirement.
    - **Users can automatically sync files across devices.**
        - Note: Sync means a change on one of your devices shows up on the others without you copying it by hand. Each device has a local Dropbox folder. Remote storage stays the copy they share.
        - You drop resume.pdf into the Dropbox folder on your laptop. The laptop uploads it to remote storage. Your phone then pulls that cloud copy into its own Dropbox folder. The phone does not read the laptop's disk.
        - The other direction works the same way. When a file lands in remote storage, each connected device pulls it into its local folder.

- Non-functional: qualities of the system
    - **The system should favor availability over consistency** (availability >> consistency)
        - Note: Same file, new version. You already shared resume.pdf. You edit it and upload the new version from India. A friend in the US can still be reading the old version for a few seconds. Dropbox still accepts your new version.
        - Note: A new file can show up late. You upload resume.pdf from your laptop. Your phone does not show it for a few seconds. That delay is okay.
        - Note: Machines near your phone and machines near a friend's phone can lose contact. Your phone can still upload. Your friend's phone can still download a file Dropbox already has. The friend may not see the brand-new file until those machines can talk again.
        - Note: Not this case (consistency >> availability). High consistency would mean that once you upload the new resume.pdf, any other device that asks Dropbox must get that new version, not the old one. If Dropbox cannot promise that yet, it waits or refuses instead of handing out the old file. We do not choose this. A friend still reading the old resume for a few seconds is fine. Stopping upload or download until every device can see the new version would make Dropbox feel down.
    - **Low Latency Uploads and Downloads**
        - How much time? File size varies, therefore, we can say as low as possible.
    - **Support large file**
        - as larges as 50gb.
        - resumable upload in case user lose internet, system shut-down, etc.
    - **High Data Integrity (sync accuracy)**
        - Yes! eventual consistency is fine. It can take couple of seconds.
        - But by the time things stablized intto a consistent manner, the integrity of our data should be high.
        - Meaning, what is in one folder, should also be in the remote storage and should also be another folder.
    - **system should be secure**
    - **system should scalability**

## 2. Core Entities
    