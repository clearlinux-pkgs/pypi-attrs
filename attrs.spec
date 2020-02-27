#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : attrs
Version  : 19.3.0
Release  : 43
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

======================================
``attrs``: Classes Without Boilerplate
======================================

.. image:: https://readthedocs.org/projects/attrs/badge/?version=stable
   :target: https://www.attrs.org/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://attrs.visualstudio.com/attrs/_apis/build/status/python-attrs.attrs?branchName=master
   :target: https://attrs.visualstudio.com/attrs/_build/latest?definitionId=1&branchName=master
   :alt: CI Status

.. image:: https://codecov.io/github/python-attrs/attrs/branch/master/graph/badge.svg
   :target: https://codecov.io/github/python-attrs/attrs
   :alt: Test Coverage

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. teaser-begin

``attrs`` is the Python package that will bring back the **joy** of **writing classes** by relieving you from the drudgery of implementing object protocols (aka `dunder <https://nedbatchelder.com/blog/200605/dunder.html>`_ methods).

Its main goal is to help you to write **concise** and **correct** software without slowing down your code.

.. -spiel-end-

For that, it gives you a class decorator and a way to declaratively define the attributes on that class:

.. -code-begin-

.. code-block:: pycon

   >>> import attr

   >>> @attr.s
   ... class SomeClass(object):
   ...     a_number = attr.ib(default=42)
   ...     list_of_numbers = attr.ib(factory=list)
   ...
   ...     def hard_math(self, another_number):
   ...         return self.a_number + sum(self.list_of_numbers) * another_number


   >>> sc = SomeClass(1, [1, 2, 3])
   >>> sc
   SomeClass(a_number=1, list_of_numbers=[1, 2, 3])

   >>> sc.hard_math(3)
   19
   >>> sc == SomeClass(1, [1, 2, 3])
   True
   >>> sc != SomeClass(2, [3, 2, 1])
   True

   >>> attr.asdict(sc)
   {'a_number': 1, 'list_of_numbers': [1, 2, 3]}

   >>> SomeClass()
   SomeClass(a_number=42, list_of_numbers=[])

   >>> C = attr.make_class("C", ["a", "b"])
   >>> C("foo", "bar")
   C(a='foo', b='bar')


After *declaring* your attributes ``attrs`` gives you:

- a concise and explicit overview of the class's attributes,
- a nice human-readable ``__repr__``,
- a complete set of comparison methods (equality and ordering),
- an initializer,
- and much more,

*without* writing dull boilerplate code again and again and *without* runtime performance penalties.

On Python 3.6 and later, you can often even drop the calls to ``attr.ib()`` by using `type annotations <https://www.attrs.org/en/latest/types.html>`_.

This gives you the power to use actual classes with actual types in your code instead of confusing ``tuple``\ s or `confusingly behaving <https://www.attrs.org/en/stable/why.html#namedtuples>`_ ``namedtuple``\ s.
Which in turn encourages you to write *small classes* that do `one thing well <https://www.destroyallsoftware.com/talks/boundaries>`_.
Never again violate the `single responsibility principle <https://en.wikipedia.org/wiki/Single_responsibility_principle>`_ just because implementing ``__init__`` et al is a painful drag.


.. -testimonials-

Testimonials
============

**Amber Hawkie Brown**, Twisted Release Manager and Computer Owl:

  Writing a fully-functional class using attrs takes me less time than writing this testimonial.


**Glyph Lefkowitz**, creator of `Twisted <https://twistedmatrix.com/>`_, `Automat <https://pypi.org/project/Automat/>`_, and other open source software, in `The One Python Library Everyone Needs <https://glyph.twistedmatrix.com/2016/08/attrs.html>`_:

  I’m looking forward to is being able to program in Python-with-attrs everywhere.
  It exerts a subtle, but positive, design influence in all the codebases I’ve see it used in.


**Kenneth Reitz**, creator of `Requests <https://github.com/psf/requests>`_ (`on paper no less <https://twitter.com/hynek/status/866817877650751488>`_!):

  attrs—classes for humans.  I like it.


**Łukasz Langa**, creator of `Black <https://github.com/psf/black>`_, prolific Python core developer, and release manager for Python 3.8 and 3.9:

  I'm increasingly digging your attr.ocity. Good job!


.. -end-

.. -project-information-

Getting Help
============

Please use the ``python-attrs`` tag on `StackOverflow <https://stackoverflow.com/questions/tagged/python-attrs>`_ to get help.

Answering questions of your fellow developers is also great way to help the project!


Project Information
===================

``attrs`` is released under the `MIT <https://choosealicense.com/licenses/mit/>`_ license,
its documentation lives at `Read the Docs <https://www.attrs.org/>`_,
the code on `GitHub <https://github.com/python-attrs/attrs>`_,
and the latest release on `PyPI <https://pypi.org/project/attrs/>`_.
It’s rigorously tested on Python 2.7, 3.4+, and PyPy.

We collect information on **third-party extensions** in our `wiki <https://github.com/python-attrs/attrs/wiki/Extensions-to-attrs>`_.
Feel free to browse and add your own!

If you'd like to contribute to ``attrs`` you're most welcome and we've written `a little guide <https://www.attrs.org/en/latest/contributing.html>`_ to get you started!


Release Information
===================

19.3.0 (2019-10-15)
-------------------

Changes
^^^^^^^

- Fixed ``auto_attribs`` usage when default values cannot be compared directly with ``==``, such as ``numpy`` arrays.
  `#585 <https://github.com/python-attrs/attrs/issues/585>`_

`Full changelog <https://www.attrs.org/en/stable/changelog.html>`_.

Credits
=======

``attrs`` is written and maintained by `Hynek Schlawack <https://hynek.me/>`_.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

A full list of contributors can be found in `GitHub's overview <https://github.com/python-attrs/attrs/graphs/contributors>`_.

It’s the spiritual successor of `characteristic <https://characteristic.readthedocs.io/>`_ and aspires to fix some of it clunkiness and unfortunate decisions.
Both were inspired by Twisted’s `FancyEqMixin <https://twistedmatrix.com/documents/current/api/twisted.python.util.FancyEqMixin.html>`_ but both are implemented using class decorators because `subclassing is bad for you <https://www.youtube.com/watch?v=3MNVP9-hglc>`_, m’kay?

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
export SOURCE_DATE_EPOCH=1582847519
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
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
