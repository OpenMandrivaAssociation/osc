Name:           osc
Version:	0.123
Release:	%mkrel 1
Summary:	OpenSUSE Build Service Commander
Group:		Development/Other
License:	GPLv2+
URL:		https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc/
# v=0.114; svn export https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc osc-$v && tar czf osc-$v.tar.gz osc-$v
Source:         osc-%{version}.tar.gz
%py_requires -d
BuildRequires:  python-urlgrabber
BuildRequires:	python-elementtree
BuildRequires:  python-m2crypto > 0.19
Requires:       python-m2crypto > 0.19
Requires:       python-urlgrabber
Requires:	python-elementtree
Requires:	python-rpm
BuildArch:      noarch

%description
Commandline client for the openSUSE Build Service.

See http://en.opensuse.org/Build_Service/CLI , as well as
http://en.opensuse.org/Build_Service_Tutorial for a general
introduction.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root %{buildroot}
ln -s osc-wrapper.py %{buildroot}/%{_bindir}/osc
mkdir -p %{buildroot}/var/lib/osc-plugins
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0755 dist/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -m 0755 dist/complete.sh %{buildroot}%{_sysconfdir}/profile.d/osc.sh
mkdir -p %{buildroot}%{_prefix}/lib/osc
install -m 0755 dist/osc.complete %{buildroot}%{_prefix}/lib/osc/complete

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/osc*
%{python_sitelib}/*
%{_sysconfdir}/profile.d/*
%dir %{_prefix}/lib/osc
%{_prefix}/lib/osc/*
%dir /var/lib/osc-plugins
%doc AUTHORS README TODO NEWS
%_mandir/man1/osc.*
