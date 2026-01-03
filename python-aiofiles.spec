%global module aiofiles
%bcond tests 1

Name:           python-%{module}
Version:        25.1.0
Release:        1
Summary:        File support for asyncio
License:        ASL 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://github.com/Tinche/aiofiles/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildRequires:  python%{pyver}dist(poetry-core)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytest-asyncio)
%endif

%description
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -v tests/
%endif

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{module}-%{version}.dist-info
%{python_sitelib}/%{module}
