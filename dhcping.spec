Summary:	DHCP daemon ping program
Summary(pl):	Program ping dla demona DHCP
Name:		dhcping
Version:	1.2
Release:	1
License:	BSD-like (?)
Group:		Networking/Utilities
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
URL:		http://www.mavetju.org/unix/general.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small tool let you perform a dhcp-request to find out if a
dhcp-server is still running.

%description -l pl
To ma³e narzêdzie wysy³a dhcp-request, aby sprawdziæ czy server DHCP
ci±gle dzia³a.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTACT
%attr(4754,root,adm) %{_bindir}/%{name}
%{_mandir}/man8/dhcping.8*
