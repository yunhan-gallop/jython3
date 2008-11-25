// Autogenerated AST node
package org.python.antlr.ast;
import java.util.ArrayList;
import org.python.antlr.AstAdapters;
import org.python.antlr.PythonTree;
import org.python.antlr.ListWrapper;
import org.antlr.runtime.CommonToken;
import org.antlr.runtime.Token;
import java.io.DataOutputStream;
import java.io.IOException;

public class Delete extends stmtType {
    private java.util.List<exprType> targets;
    public java.util.List<exprType> getInternalTargets() {
        return targets;
    }
    public Object getTargets() {
        return new ListWrapper(targets);
    }
    public void setTargets(Object targets) {
        this.targets = AstAdapters.to_exprList(targets);
    }


    private final static String[] fields = new String[] {"targets"};
    public String[] get_fields() { return fields; }

    public Delete() {}
    public Delete(Object targets) {
        setTargets(targets);
    }

    public Delete(Token token, java.util.List<exprType> targets) {
        super(token);
        this.targets = targets;
        if (targets == null) {
            this.targets = new ArrayList<exprType>();
        }
        for(PythonTree t : this.targets) {
            addChild(t);
        }
    }

    public Delete(Integer ttype, Token token, java.util.List<exprType> targets)
    {
        super(ttype, token);
        this.targets = targets;
        if (targets == null) {
            this.targets = new ArrayList<exprType>();
        }
        for(PythonTree t : this.targets) {
            addChild(t);
        }
    }

    public Delete(PythonTree tree, java.util.List<exprType> targets) {
        super(tree);
        this.targets = targets;
        if (targets == null) {
            this.targets = new ArrayList<exprType>();
        }
        for(PythonTree t : this.targets) {
            addChild(t);
        }
    }

    public String toString() {
        return "Delete";
    }

    public String toStringTree() {
        StringBuffer sb = new StringBuffer("Delete(");
        sb.append("targets=");
        sb.append(dumpThis(targets));
        sb.append(",");
        sb.append(")");
        return sb.toString();
    }

    public <R> R accept(VisitorIF<R> visitor) throws Exception {
        return visitor.visitDelete(this);
    }

    public void traverse(VisitorIF visitor) throws Exception {
        if (targets != null) {
            for (PythonTree t : targets) {
                if (t != null)
                    t.accept(visitor);
            }
        }
    }

    private int lineno = -1;
    public int getLineno() {
        if (lineno != -1) {
            return lineno;
        }
        return getLine();
    }

    public void setLineno(int num) {
        lineno = num;
    }

    private int col_offset = -1;
    public int getCol_offset() {
        if (col_offset != -1) {
            return col_offset;
        }
        return getCharPositionInLine();
    }

    public void setCol_offset(int num) {
        col_offset = num;
    }

}
