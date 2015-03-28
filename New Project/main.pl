#
# Hello World Program in Perl
#
print "Hello World!\n";

#
# Hello World Program in Perl
#
print "Hello World!\n";

use strict;
use warnings;

sub max {
    my ($x, $y) = @_;
    if ($x > $y)  {$x} else {$y}
    }
print max(4,1)."\n";

sub max_of_three {
    my ($x, $y, $z) = @_;
    if ( $x > $y and $x > $z) {$x} elsif ($y > $z) {$y} else {$z}
}
print max_of_three (5,9,1)."\n";

sub find_length {
    my ($x) = @_;
    my $count =0;
    foreach (split //, $x) {$count += 1;}
    $count;
    }
    
print find_length("tanmay")."\n";

sub find_vowel {
    if ($_[0] eq 'a' or $_[0] eq 'e' or $_[0] eq 'i' or $_[0] eq 'o' or $_[0] eq "u")
    {"A vowel"} else {"Not a vowel"}
    }
print find_vowel("u")."\n";
print find_vowel('z')."\n";

sub translate {
    my ($x) = @_;
    $x =~ s/([^ aeiou])/\1o\1/g; # exluce splace, aeiou, do global
    $x;
}
print translate("this is fun")."\n";

sub sum {
    my $count=0;
    foreach (@_) { $count += $_;}
    $count;
    }
sub multiply {
    my $count=1;
    foreach (@_) { $count *= $_;}
    $count;
}
print &sum(1,2,3,4,5)."\n";
print multiply(1,2,3,4,5)."\n";

sub reverse1 {
    my ($x) = @_; 
    my $reversed ='';
    foreach  ( 1..length($x)) {$reversed .= substr($x, -$_, 1) ;}
    # you can only access nth character of a string using substring it's not python :P
    $reversed;
    }
print reverse1("how are you?")."\n";


sub is_palindrome {
    my ($x) = @_;
    if ($x eq reverse1($x)){"is palindrome"} else {"Not a palindrome"} #cannot use == operator
    }
print is_palindrome("radar")."\n";


sub is_member {
    my ($x, @list) = @_;
    foreach (@list) { 
        if ($x eq ($_)) {return "contains";} else {return "doesn't contain"}
        }
    }
  
my @a = qw(apple x orange but so nos how dod to it a b c);
print is_member("apple",@a)."\n";

sub overlapping {
    my ($a, $b) = @_;
    my @list1 = @$a;
    my @list2 = @$b;
    foreach my $x (@list1) {
        foreach my $y (@list2) {
            if ($x eq $y) {return "contains"} else {return "doesn't contain"}
        }
    }
}
my @array1 = qw/a b c d /;
my @array2 = qw/e f g h/;
print overlapping(\@array1, \@array2)."\n";

sub generate_n_chars{
    my ($n, $c) = @_;
    my $x = $c; # to store initial value of $c
    for (1..$n-1) {
    $c .= $x;
    }
    return $c;
}
print generate_n_chars(5,'a'), "\n";

    
sub histogram {
    my @a = @_;
    my $histogram ='';
    foreach (@_) {
        $histogram .= generate_n_chars($_,'*');
        $histogram .= "\n";
    }
    return $histogram;
    }
    
print histogram(1,4,9,7,3,2)."\n";


sub max_in_list {
    my ($x) = shift (@_);
    foreach (@_) {
        if ( $x> $_) { return $x;} else { $x=$_;}
    }
    return $x; # in case if last no. is max, the loop would already be over. 
}
        
print max_in_list(1,2,3,192,4,5,6,7,8)."\n";

sub words_to_integers {
    my @list;
    foreach (@_) {
        push (@list,length($_));
    }
    return join (" ", @list); # return @list will return just the last index of the list #remember this is returning a string
    }
print words_to_integers('pomengrenate','orange','banana','kiwi','berry','cherry')."\n";


sub find_longest_word {
    my $x = words_to_integers(@_);
    my @words = split(/ /,$x);
    return max_in_list(@words);
}
print find_longest_word('new','what','schizophrenia')."\n";













