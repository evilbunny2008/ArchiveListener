""" Installer for ArchiveListenerService. """

from weecfg.extension import ExtensionInstaller

VERSION = "0.0.2"

def loader():
    """ Load and return the extension installer """
    return ArchiveListenerInstaller()

class ArchiveListenerInstaller(ExtensionInstaller):
    """ The extension installer. """
    def __init__(self):

        install_dict = {
            'version': VERSION,
            'name': 'ArchiveListener',
            # add a leading space, so that long versions does not run into the description
            'description': ' Simple WeeWX user script to dump the contents of an archive record',
            'author': "John Smith",
            'author_email': "deltafoxtrot256+ArchiveListener@gmail.com",
            'files': [('bin/user', ['bin/user/archive_listener.py'])],
            'report_services': 'user.archive_listener.ArchiveListenerService',
        }

        super().__init__(install_dict)
