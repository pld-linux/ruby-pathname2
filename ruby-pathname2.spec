#
%define tarname pathname2
Summary:	Path name manipulation library
Name:		ruby-pathname2
Version:	1.5.2
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/18293/pathname2-%{version}.tar.bz2
# Source0-md5:	3fba84e5eb164e932c2c9b2206537bff
URL:		http://shards.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Path name manipulation library.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/*
%{ruby_ridir}/Pathname*
