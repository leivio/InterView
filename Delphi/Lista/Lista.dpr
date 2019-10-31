program Lista;

uses Sysutils;

type

  TBox = class
  private
    FValue: Integer;
    FPrior: TBox;
    FNext: TBox;
  public
     constructor Create(APrior:TBox = nil; AValue: Integer = 0); reintroduce;
     property Prior: TBox read FPrior write FPrior;
     property Next: TBox read FNext write FNext;
     Property Value: Integer read FValue write FValue;
  end;

var
  i, j: Integer;
{ TBox }

constructor TBox.Create(APrior: TBox; AValue: Integer);
begin
 FPrior := APrior;
 FValue := AValue;

 if Assigned(FPrior) then
   FPrior.Next := Self;
end;

var
  Box :TBox;
  Obj: TObject;
begin
  Box := nil;
// Define
  for i := 1 to 10 do
    Box := TBox.Create(Box, i);
// Show
  repeat
    Writeln(' ->' +  Inttostr(Box.value));
    Box := Box.Prior;
  until Box.prior = nil;
  Writeln(' ->' +  Inttostr(Box.value));

// Free Mem
  while Assigned(Box.Next) do
  begin
    Writeln(' Free ->' +  Inttostr(Box.value));
    Obj := Box;
    Box := Box.Next;
    Obj.free;
  end;

  Readln(J);
end.
