#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : pypi-attrs
Version  : 21.4.0
Release  : 67
URL      : https://files.pythonhosted.org/packages/d7/77/ebb15fc26d0f815839ecd897b919ed6d85c050feeb83e100e020df9153d2/attrs-21.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d7/77/ebb15fc26d0f815839ecd897b919ed6d85c050feeb83e100e020df9153d2/attrs-21.4.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/d7/77/ebb15fc26d0f815839ecd897b919ed6d85c050feeb83e100e020df9153d2/attrs-21.4.0.tar.gz.asc
Summary  : Classes Without Boilerplate
Group    : Development/Tools
License  : MIT
Requires: pypi-attrs-license = %{version}-%{release}
Requires: pypi-attrs-python = %{version}-%{release}
Requires: pypi-attrs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. raw:: html
<p align="center">
<a href="https://www.attrs.org/">
<img src="./docs/_static/attrs_logo.svg" width="35%" alt="attrs" />
</a>
</p>
<p align="center">
<a href="https://www.attrs.org/en/stable/?badge=stable">
<img src="https://img.shields.io/badge/Docs-Read%20The%20Docs-black" alt="Documentation" />
</a>
<a href="https://github.com/python-attrs/attrs/blob/main/LICENSE">
<img src="https://img.shields.io/badge/license-MIT-C06524" alt="License: MIT" />
</a>
<a href="https://pypi.org/project/attrs/">
<img src="https://img.shields.io/pypi/v/attrs" />
</a>
</p>

%package license
Summary: license components for the pypi-attrs package.
Group: Default

%description license
license components for the pypi-attrs package.


%package python
Summary: python components for the pypi-attrs package.
Group: Default
Requires: pypi-attrs-python3 = %{version}-%{release}

%description python
python components for the pypi-attrs package.


%package python3
Summary: python3 components for the pypi-attrs package.
Group: Default
Requires: python3-core
Provides: pypi(attrs)

%description python3
python3 components for the pypi-attrs package.


%prep
%setup -q -n attrs-21.4.0
cd %{_builddir}/attrs-21.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642003244
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-attrs
cp %{_builddir}/attrs-21.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-attrs/00ff890e8493d10b07d5d3fafa23639bb071e443
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-attrs/00ff890e8493d10b07d5d3fafa23639bb071e443

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
