from distutils.core import setup
setup(
  name = 'zoho_oauth2',         # How you named your package folder (MyLib)
  packages = ['zoho_oauth2'],   # Chose the same as "name"
  version = '1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implements OAuth2.0 flow to use ManageEngine Service Desk API.',   # Give a short description about your library
  author = 'Saurav Koli',                   # Type in your name
  author_email = 'sauravkoli3105@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sauravkoli31/zoho_oauth2',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sauravkoli31/zoho_oauth2/archive/refs/tags/1.2.tar.gz',    # I explain this later on
  keywords = ['zoho', 'ZohoAPI', 'ZOHO API', 'Manage Engine'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)