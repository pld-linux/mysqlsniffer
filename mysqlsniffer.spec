Summary:	Dumps packets that are sent or received over a network interface
Summary(pl.UTF-8):	Zrzucanie pakietów wysyłanych lub otrzymywanych po interfejsie sieciowym
Name:		mysqlsniffer
Version:	1.2
Release:	5
License:	GPL
Group:		Applications/Networking
Source0:	http://hackmysql.com/code/%{name}.tgz
# Source0-md5:	816575bfd06179192468a15dd3d26cdb
URL:		http://hackmysql.com/mysqlsniffer
BuildRequires:	libpcap-devel >= 2:0.8.3-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlsniffer is a tcpdump clone for watching MySQL traffic on a
network. Coded in C using the pcap library, mysqlsniffer captures and
interprets MySQL traffic on a TCP/IP network.

%description -l pl.UTF-8
mysqlsniffer to klon tcpdumpa do podglądania ruchu MySQL-a w sieci.
Jest napisany w C z użyciem biblioteki pcap. Wyłapuje i interpretuje
ruch MySQL-a w sieci TCP/IP.

%prep
%setup -q -c

%build
%{__cc} %{rpmcflags} -Wall -fPIC -c *.c
%{__cc} %{rpmcflags} %{rpmldflags} -Wall -o mysqlsniffer *.o -lpcap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
