%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Google
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Provides access to the Google Web APIs
Summary(pl):	%{_pearname} - Dost�p do API stron Google
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fcbd0d69394ba7877926937ba9a3b3d6
URL:		http://pear.php.net/package/Services_Google/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows easy access to the Google Web APIs for the search engine,
spelling suggestions, and cache.

To use the package you'll need an API key from
http://www.google.com/apis/ .

In PEAR status of this package is: %{_status}.

%description -l pl
Pozwala na �atwy dost�p do API stron Google - wyszukiwarki, porad
dotycz�cych pisowni oraz cache.

Aby u�y� tego pakietu potrzebny b�dzie klucz API ze strony
http://www.google.com/apis/ .

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
