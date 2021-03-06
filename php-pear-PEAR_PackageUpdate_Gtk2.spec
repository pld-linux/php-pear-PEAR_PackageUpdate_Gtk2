%define		_status		beta
%define		_pearname	PEAR_PackageUpdate_Gtk2
Summary:	%{_pearname} - A PHP-GTK 2 front end for PEAR_PackageUpdate
Summary(pl.UTF-8):	%{_pearname} - Frontend PHP-GTK2 do PEAR_PackageUpdate
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5f8ee6f220a110890d35cfdc5919eda
URL:		http://pear.php.net/package/PEAR_PackageUpdate_Gtk2/
BuildRequires:	php-pear-PEAR >= 1:1.4.8
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.-0.8
Requires:	php-pear-PEAR_PackageUpdate >= 0.3.0-0.devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

PEAR_PackageUpdate (PPU) is designed to allow developers to easily
include auto updating features for other packages and PEAR installable
applications. PPU will check to see if a new version of a package is
available and then ask the user if they would like to update the
package. PPU uses PEAR to communicate with the channel server and to
execute the update.

PPU allows the end user to take some control over when they are
notified about new releases. The PPU Preferences allow a user to tell
PPU not to ask about certain types of releases (bug fixes, minor
releases, etc.), not to ask about certain release states (devel,
alpha, etc.), not to ask until the next release or not to ask again.

PEAR_PackgeUpdate_Gtk2 is a PHP-GTK 2 front end for PPU. It is
designed to be used by PHP-GTK 2 packages and applications that want
to include auto-updating features.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR_PackageUpdate (PPU) został zaprojektowany aby umożliwić
developerom dołączenie w prosty sposób automatycznej aktualizacji
innych pakietów PEAR lub aplikacji korzystających ze sposobu
instalacji PEAR. PPU sprawdzi czy jest dostępna nowa wersja i zapyta
użytkownika czy chciałby zaktualizować pakiet. PPU korzysta z PEAR do
komunikacji z serwerem kanałów oraz do wykonania aktualizacji.

PPU pozwala użytkownikowi końcowemu na pewną kontrolę kiedy mają być
powiadamiania o nowych aktualizacjach. Preferencje PPU pozwalają
użytkownikowi na pominięcie pewnych rodzajów aktualizacji (poprawki
błędów, drobne wydania), czy konkretnych statusów (devel, alpha,
itp.), czy polecenie PPU aby nie pytał do czasu kolejnej wersji.

PEAR_PackageUpdate_Gtk2 jest opartym o PHP-GTK 2 frontendem do PPU.
Został zaprojektowany w celu dołączenia do aplikacji korzystających z
PHP-GTK 2 funkcji automatycznej aktualizacji.

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
%doc install.log docs/%{_pearname}/ppuExample.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageUpdate/Gtk2.php
