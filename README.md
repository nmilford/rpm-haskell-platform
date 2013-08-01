rpm-haskell-platform
====================

An RPM spec file to build and install the Haskell Platform.

To Build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`sudo yum -y install gmp-devel freeglut-devel zlib-devel ghc`

`wget http://lambda.haskell.org/platform/download/2013.2.0.0/haskell-platform-2013.2.0.0.tar.gz -O ~/rpmbuild/SOURCES/haskell-platform-2013.2.0.0.tar.gz`

`wget https://raw.github.com/nmilford/rpm-haskell-platform/master/install.sh -O ~/rpmbuild/SOURCES/install.sh`

`wget https://raw.github.com/nmilford/rpm-haskell-platform/master/haskell-platform.spec -O ~/rpmbuild/SPECS/haskell-platform.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/haskell-platform.spec`
