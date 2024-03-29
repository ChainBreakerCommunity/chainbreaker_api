
from distutils.core import setup
setup(
  name = 'chainbreaker_api',         # How you named your package folder (MyLib)
  packages = ['chainbreaker_api'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python library for connecting and using ChainBreaker Community Services.',   # Give a short description about your library
  author = 'Juan Cepeda',                   # Type in your name
  author_email = 'juancepeda.gestion@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ChainBreakerCommunity/chainbreaker_api',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ChainBreakerCommunity/chainbreaker_api/archive/refs/tags/1.0.4.tar.gz',    # I explain this later on
  keywords = ['CHAINBREAKER', 'API', 'HUMAM TRAFFICKING'],   # Keywords that define your package best
  
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'requests',
          'urllib3',
          'chainbreaker_api'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)