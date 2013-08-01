# To Build:
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install gmp-devel freeglut-devel zlib-devel
# wget http://lambda.haskell.org/platform/download/2013.2.0.0/haskell-platform-2013.2.0.0.tar.gz -O ~/rpmbuild/SOURCES/haskell-platform-2013.2.0.0.tar.gz 
# wget https://raw.github.com/nmilford/rpm-haskell-platform/master/install.sh -O ~/rpmbuild/SOURCES/install.sh
# wget https://raw.github.com/nmilford/rpm-haskell-platform/master/haskell-platform.spec -O ~/rpmbuild/SPECS/haskell-platform.spec
# rpmbuild -bb ~/rpmbuild/SPECS/haskell-platform.spec

%define ghc_dir %(cat $(which ghc) | grep exedir | head -1 | cut -f2 -d'"')
%define ghc_pkg_dir %{ghc_dir}/package.conf.d/

Name:           haskell-platform
Version:        2013.2.0.0
Release:        1
Summary:        Standard Haskell libraries and tools 
Group:          Development/Languages
License:        BSD
URL:            http://www.haskell.org/platform/
Source0:        http://lambda.haskell.org/platform/download/%{version}/%{name}-%{version}.tar.gz
# Based on http://trac.haskell.org/haskell-platform/ticket/196
Source1:        install.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ghc
BuildRequires:  freeglut-devel
BuildRequires:  gmp-devel
BuildRequires:  zlib-devel
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildArch:      x86_64
Requires:       coreutils
Requires:       gcc
Requires:       make
Requires:       gmp-devel
Requires:       ghc
Requires:       zlib-devel

%description
The Haskell Platform is a comprehensive, robust development environment for 
programming in Haskell. For new users the platform makes it trivial to get up
and running with a full Haskell development environment. For experienced 
developers, the platform provides a comprehensive, standard base for commercial
and open source Haskell development that maximises interoperability and
stability of your code.

%prep
%setup -q -n %{name}-%{version}
rm -f %{_builddir}/%{name}-%{version}/scripts/install.sh
install -m 755 %_sourcedir/install.sh %{_builddir}/%{name}-%{version}/scripts/install.sh

%build
./configure
make 

%install
install -d -m 755 %{buildroot}/load
make --directory=%_builddir/%{name}-%{version} DESTDIR=%{buildroot} install

install -d -m 755 %{buildroot}/%{ghc_pkg_dir}
mv %{buildroot}/load/*.conf %{buildroot}/%{ghc_pkg_dir} 
rm -rf %{buildroot}/load

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/lib/*
/usr/local/share/*
/usr/local/bin/*
%{ghc_pkg_dir}/*

%post
%{_bindir}/ghc-pkg recache

%changelog
* Wed Jul 31 2013 Nathan Milford <nathan@milford.io> 2013.2.0.0
- Initial spec.