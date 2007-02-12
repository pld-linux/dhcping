Summary:	DHCP daemon ping program
Summary(pl.UTF-8):   Program ping dla demona DHCP
Name:		dhcping
Version:	1.2
Release:	2
License:	BSD-like (?)
Group:		Networking/Utilities
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c4b22bbf3446c8567e371c40aa552d5d
URL:		http://www.mavetju.org/unix/general.php
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small tool let you perform a dhcp-request to find out if a
dhcp-server is still running.

%description -l pl.UTF-8
To małe narzędzie wysyła dhcp-request, aby sprawdzić czy server DHCP
ciągle działa.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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
