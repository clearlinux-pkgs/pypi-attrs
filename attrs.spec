#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : attrs
Version  : 19.3.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/98/c3/2c227e66b5e896e15ccdae2e00bbc69aa46e9a8ce8869cc5fa96310bf612/attrs-19.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/c3/2c227e66b5e896e15ccdae2e00bbc69aa46e9a8ce8869cc5fa96310bf612/attrs-19.3.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/98/c3/2c227e66b5e896e15ccdae2e00bbc69aa46e9a8ce8869cc5fa96310bf612/attrs-19.3.0.tar.gz.asc
Summary  : Classes Without Boilerplate
Group    : Development/Tools
License  : MIT
Requires: attrs-license = %{version}-%{release}
Requires: attrs-python = %{version}-%{release}
Requires: attrs-python3 = %{version}-%{release}
Requires: six
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
.. image:: https://www.attrs.org/en/latest/_static/attrs_logo.png
:alt: attrs Logo

%package license
Summary: license components for the attrs package.
Group: Default

%description license
license components for the attrs package.


%package python
Summary: python components for the attrs package.
Group: Default
Requires: attrs-python3 = %{version}-%{release}

%description python
python components for the attrs package.


%package python3
Summary: python3 components for the attrs package.
Group: Default
Requires: python3-core
Provides: pypi(attrs)

%description python3
python3 components for the attrs package.


%prep
%setup -q -n attrs-19.3.0
cd %{_builddir}/attrs-19.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603387696
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/attrs
cp %{_builddir}/attrs-19.3.0/LICENSE %{buildroot}/usr/share/package-licenses/attrs/00ff890e8493d10b07d5d3fafa23639bb071e443
cp %{_builddir}/attrs-19.3.0/docs/license.rst %{buildroot}/usr/share/package-licenses/attrs/189f457bcddb4a83cda90f30f1e21a2a2d1504a3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/attrs/00ff890e8493d10b07d5d3fafa23639bb071e443
/usr/share/package-licenses/attrs/189f457bcddb4a83cda90f30f1e21a2a2d1504a3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
