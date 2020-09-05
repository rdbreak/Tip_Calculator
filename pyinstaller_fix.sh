#!/bin/bash
echo "Installing Dependencies"
brew install zlib
brew install sqlite
brew install bzip2
brew install libiconv
brew install curl
brew install libzip
echo "Done!"
echo
echo -e "Setting Environment Variables"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
echo "Done!"
echo
echo "Installing Python 3.8.5"
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.5
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.8.5
echo "Done!"
exit 0
