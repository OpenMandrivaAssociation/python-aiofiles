%global module aiofiles

Name:           python-%{module}
Version:        23.2.1
Release:        1
Summary:        File support for asyncio
License:        ASL 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://github.com/Tinche/aiofiles/archive/v%{version}/%{module}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(poetry-core)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytoml)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

BuildArch:      noarch

%description
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{module}-*-info/
%{python_sitelib}/%{module}/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

