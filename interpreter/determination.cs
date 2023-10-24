namespace Freell
{
    public class Determination
    {
        public bool Valid { get; set; }
        public string Suggestion { get; set; }

        public Determination(bool valid, string suggestion)
        {
            this.Valid = valid;
            this.Suggestion = suggestion;
        }
    }
}
