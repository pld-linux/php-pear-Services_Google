%define		_status		alpha
%define		_pearname	Services_Google
Summary:	%{_pearname} - Provides access to the Google Web APIs
Summary(pl.UTF-8):	%{_pearname} - Dostęp do API stron Google
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8960f656886605df9dff31faa7d8d10b
URL:		http://pear.php.net/package/Services_Google/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0
Requires:	php(soap)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows easy access to the Google Web APIs for the search engine,
spelling suggestions, and cache.

To use the package you'll need an API key from
<http://www.google.com/apis/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pozwala na łatwy dostęp do API stron Google - wyszukiwarki, porad
dotyczących pisowni oraz cache.

Aby użyć tego pakietu potrzebny będzie klucz API ze strony
<http://www.google.com/apis/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/*.php
