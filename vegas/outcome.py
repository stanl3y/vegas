class Outcome(object):
  def __init__(self, name, odds):
    """Constructor."""
    self.name = name
    self.odds = odds

  def winAmount(self, amount):
    """Calculate the winnings given the amount bet."""
    return amount * self.odds

  def __eq__(self, other):
    """Check for equality with another Outcome."""
    return self.name == other.name

  def __ne__(self, other):
    """Check for inequality with another Outcome."""
    return not self.__eq__(other)

  def __hash__(self):
    """Return the hash code of an Outcome."""
    return hash(self.name)

  def __str__(self):
    """Return a human readable representation."""
    return "{} ({}:1)".format(self.name, self.odds)

  def __repr__(self):
    """Return a machine readable representation."""
    return "{class_}({name!r}, {odds!r})".format(class_=Outcome.__name__, **vars(self))
