Name:		osc
Version:	0.144
Release:	2
Summary:	OpenSUSE Build Service Commander
Group:		Development/Other
License:	GPLv2+
URL:		https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc/
Source0:	%{name}-%{version}.tar.gz
Source1:	complete.csh
Source2:	complete.sh
Source3:	osc.complete
BuildRequires:	python-elementtree
BuildRequires:	pythonegg(m2crypto)
BuildRequires:	pythonegg(urlgrabber)
Requires:	python-elementtree
Requires:	pythonegg(m2crypto)
Requires:	pythonegg(urlgrabber)
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
