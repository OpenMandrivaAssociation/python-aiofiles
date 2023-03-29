%global modname aiofiles

Name:           python-%{modname}
Version:        23.1.0
Release:        1
Summary:        File support for asyncio

License:        ASL 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://github.com/Tinche/aiofiles/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-asyncio)

%{?python_provide:%python_provide python3-%{modname}}

BuildArch:      noarch

%description
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py_build

%install
%py_install


%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{modname}-*-info/
%{python_sitelib}/%{modname}/
