Name:		osc
Version:	0.174.0
Release:	1
Summary:	OpenSUSE Build Service Commander
Group:		Development/Other
License:	GPLv2+
URL:		https://github.com/openSUSE/osc
Source0:	https://github.com/openSUSE/osc/archive/refs/tags/0.174.0.tar.gz
Source1:	complete.csh
Source2:	complete.sh
Source3:	osc.complete
BuildRequires:	python-elementtree
BuildRequires:	python3dist(m2crypto)
BuildRequires:	python3dist(urlgrabber)
BuildRequires:	python3dist(setuptools)
Requires:	python-elementtree
Requires:	python3dist(m2crypto)
Requires:	python3dist(urlgrabber)
Requires:	python-rpm
BuildArch:	noarch

%description
Commandline client for the openSUSE Build Service.

See http://en.opensuse.org/Build_Service/CLI , as well as
http://en.opensuse.org/Build_Service_Tutorial for a general
introduction.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root %{buildroot}
ln -s osc-wrapper.py %{buildroot}%{_bindir}/osc
mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins
install -m644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -m644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/profile.d/osc.sh
install -m755 %{SOURCE3} -D %{buildroot}%{_prefix}/lib/osc/complete

%files
%doc README
%{_bindir}/osc*
%{python_sitelib}/*
%{_sysconfdir}/profile.d/*
%dir %{_prefix}/lib/osc
%{_prefix}/lib/osc/*
%dir /var/lib/osc-plugins
%{_mandir}/man1/osc.1*
