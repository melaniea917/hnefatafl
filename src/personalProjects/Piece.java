package personalProjects;

/**
 * The class for determining the state of the board pieces
 *
 * @Author Richard Erickson and Melanie Andromidas
 * @Version 0.0.1
 */
public class Piece {
    private boolean isCaptured;
    private boolean hasEscaped;
    private Type type;

    public Piece(Type piece) {
        isCaptured = false;
        hasEscaped = false;
        type = piece;
    }
}
