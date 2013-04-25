Name:		osc
Version:	0.139.2
Release:	1
Summary:	OpenSUSE Build Service Commander
Group:		Development/Other
License:	GPLv2+
URL:		https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc/
# v=0.114; svn export https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc osc-$v && tar czf osc-$v.tar.gz osc-$v
Source0:	%{name}-%{version}.tar.gz
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
install -m644 dist/complete.csh -D %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -m644 dist/complete.sh -D %{buildroot}%{_sysconfdir}/profile.d/osc.sh
install -m755 dist/osc.complete -D %{buildroot}%{_prefix}/lib/osc/complete

%files
%doc AUTHORS README TODO NEWS
%{_bindir}/osc*
%{python_sitelib}/*
%{_sysconfdir}/profile.d/*
%dir %{_prefix}/lib/osc
%{_prefix}/lib/osc/*
%dir /var/lib/osc-plugins
%{_mandir}/man1/osc.1*

%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.123-2mdv2011.0
+ Revision: 593922
- rebuild for py2.7

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 0.123-1mdv2010.1
+ Revision: 468054
- add buildroot
- import osc

