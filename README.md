# sagemath-bootcamp

This repository represents my playground for exploring the beautiful software system SageMath which plays a fundamental role in all of my research. The code does not follow any particular structure and is most likely not up to date.

The code might be given in the form of Jupyter notebooks, standalone Python scripts which use the Sage library or by writing interpreted and compiled programs in Sage directly. The last option will most likely stay an exception.

## Graph Theory

A graph is a set $G=(V, E)$ of sets satisfying $E \subseteq [V]^2$. The elements of $V$ are called vertices, the elements of $E$ are called edges. Sometimes we simply write $G$ and denote the set of vertices of $G$ by $V(G)$ and the set of edges of $G$ by $E(G)$. A self-loop is an edge $(v,v) \in E$, that is, a vertex connected to itself. A graph might have multiple edges connecting one vertex to another, that is, an edge $(v_x, v_y) \in E$ might appear multiple times. A graph is called *simple* graph if it does not admit self-loops or multiple edges. If we endow the set $E$ with a partial order, then the corresponding graph $G$ is called a *directed* graph. A graph is undirected if the set $E$ is not endowed with a partial order, that is any pair $(v_x, v_y)$ in $E$ is unordered. A graph is called *finite* if its set of vertices and its set of edges is finite.

Therefore, a graph is a discrete structure endowing all pairs of $V$ with a binary relation. Notice that this might be generalized to a so called *hypergraph*, that is a graph which allows its edges to contain any number of vertices and thus it is endowed with a $k$-nary relation on $V$. We might talk about this in more detail at another point of this article.

Graphs are usually introduced with its *natural* representation which uses dots for its vertices and lines for its edges. We make this rigorous by introducing the topology of graphs.

A *topology* on a set $X$ is a collection $\mathcal{T}$ of subsets of $X$ having the following properties:

(i) $\emptyset, X \in \mathcal{T}$

(ii) The union of the elements of any subcollection of $\mathcal{T}$ is in $\mathcal{T}$.

(iii) The intersection of the elements of any finite subcollection of $\mathcal{T}$ is in $\mathcal{T}$.

Given a topology $\mathcal{T}$ on a set $X$. The ordered pair $(X, \mathcal{T})$ is called a *topological space*. The elements of $\mathcal{T}$ are called *open sets*. We sometimes denote a topological space just by the set $X$ if its topology is clear from the context. A subset $A$ of a topological space $(X, \mathcal{T})$ is said to be *closed* if the set $X-A$ is open. A subset $A$ of a topological space $X$ is called *clopen* if it is both open and closed in $X$. It is easy to see that both $X$ and $\emptyset$ are clopen sets.

Let $X$ be a topological space. A *separation* of $X$ is a pair $(U, V)$ of disjoint nonempty open subsets of $X$ whose union is $X$. The space $X$ is said to be *connected* if there does not exist a separation of $X$. Let $X$ and $Y$ be topological spaces. A function $f: X \to Y$ is said to be *continuous* if for each open subset $V$ of $Y$, the set $f^{-1}(V)$ is an open subset of $X$. Let $X$ and $Y$ be topological spaces. Let $\phi: X \to Y$ be a bijection. If both the function $\phi$ and the inverse function $\phi^{-1}: Y \to X$ are continuous, then $\phi$ is called an *homeomorphism*. We say that $X$ and $Y$ are *homeomorphic* and write $X \simeq Y$.

A *straight line segment* in the euclidian plane is a subset of $\mathbb{R}^2$ that has the form $L=\{p+\lambda(q-p)\ |\ 0 \leq \lambda \leq 1\}$ for distinct points $p,q$ in $\mathbb{R}^2$. Instead of *straight line segment*, we shall simply say *line segment*. A *polygonal arc* is a subset of $\mathbb{R}^2$ which is the union of finitely many straight line segments and is homeomorphic to the closed unit interval $I_1=[0,1]$. The images of $0$ and $1$ under such a homeomorphism are the *endpoints* of this polygonal arc, which *links* them and *runs* between them. Instead of *polygonal arc* we shall simply say *arc*. It is easy to see that an arc is homeomorphic to the unit interval. If $P$ is an arc between two points $x$ and $y$, we call the point set $P \setminus \{x,y\}$ the *interior* of *P*. A *polygon* is a subset of $\mathbb{R}^2$, which is the union of finitely many straight line segments and is homeomorphic to the unit circle $S^1$.

Let $\mathcal{O} \subseteq \mathbb{R}^2$ be any open set. Being linked by an arc in $\mathcal{O}$ defines an equivalence relation on $\mathcal{O}$. The corresponding equivalence classes are again open. They are the *regions* of $\mathcal{O}$. A closed set $X \subseteq \mathbb{R}^2$ is said to *separate* a region $\mathcal{O}'$ of $\mathcal{O}$ if $\mathcal{O}' \setminus X$ has more than one region. 

A *plane graph* is a pair $(V, E)$ of finite sets with the following properties:

(i) $V \subseteq \mathbb{R}^2$

(ii) Every edge is an arc between two vertices

(iii) Different edges have different sets of endpoints

(iv) The interior of an edge contains not vertex and no point of any other edge

The abstract graph of a plane graph is called *planar graph*. As long as no confusion arises, we shall use the same name for the abstract graph and its plane graph.

When $G$ is a plane graph, we call the regions of $\mathbb{R}^2 \setminus G$ the *faces* of $G$. These are open subsets of $\mathbb{R}^2$. Since $G$ is bounded, exactly one of its faces is unbounded. This face is the *outer face* of $G$. The other faces are its *inner faces*. An embedding in the plane, or *planar embedding*, of an abstract graph $G$ is an isomorphism between $G$ and a plane graph $G'$. The latte will be called *drawing* of $G$. We shall not always distinguish notationally between the vertices and edges of $G$ and $G'$.

We consider a graph $G=(V,E)$ with $V=\{v_0, v_1, v_2\}$ and $E=\{(v_0,v_1),(v_0,v_2), (v_1, v_2)\}$ in order to provide an example. The graph $G$ defines a complete graph on three vertices. Define $X=\mathbb{R}^2 \setminus G$, then $X$ is open in $\mathbb{R}^2$. The set $X$ is the union of two disjoint subsets $I=\mathbb{R}^2 \setminus (G \cup O)$ and $O=\mathbb{R}^2 \setminus (G\cup I)$, They are the regions of $X$ and are by definition again open in $\mathbb{R}^2$. To summarize, we define a topology on $\mathbb{R}^2$ by $\mathcal{T}=\{\mathbb{R}^2, \emptyset, X, I, O\}$. Notice that $G$ is closed, since $X$ is open. And implicitly $I \cap O=\emptyset \in \mathcal{T}, I \cup O =X \in \mathcal{T}, I \cup X=X,O\cup X=X, X \cap I=I, X \cap O =O$.

Notice that we have introduced the topology of planar graphs, that are graphs in which no edge crosses. The above considerations can be generalized to graphs for which the crossing of edges are allowed.

Now, that we have introduced abstract graphs and its topological representation, we are going to explore them using SageMath.

## Group Theory

A set $G$ is a group if the following criteria are satisfied:

1. There is a binary operation $*$ on $G$.
2. $*$ is associative.
3. There is an identity element $e \in G$. That is: $$e*g=g=g*e, \forall g \in G.$$
4. Every element $g \in G$ has an inverse, $g^{-1}$, satisfying $$g*g^{-1}=e=g^{-1}*g.$$

We call the members of a group elements and use basic set theory notation.

If $*$ is a binary operation on a set $S$, then $s*t \in S$ for all $s,t$ in $S$. In this case, we say that $S$ is *closed* under the operation $*$. Combining two group elements is a binary operation and we say that it is a binary operation on the group. A binary operation $*$ on a set $S$ is called associative if it satisfies the associative law: $$(x*y)*z=x*(y*z), \forall x,y,z \in S.$$
A group $(G, *)$ is called *abelian* if $a*b=b*a$ for all $a,b$ in $G$.

A *generator* of a group is an element of the group such that any other element of the group can be generated by combining the generator with itself using the binary operation of the group. Usually, a single element is not enough in order to generate the whole group. A *generating* set for a group is a subcollection of elements of the group that together can produce all elements of the group. All elements of this subcollection are called generators in this case. We write $G=\langle g_x, g_y \rangle$ to say that $G$ is generated by the elements of $g_x$ and $g_y$


Now, that we have introduced groups, we are going to explore them using SageMath.

## References

[1] Reinhard Diestel. Graph Theory (Graduate Texts in mathematics). 5th ed. Vol. 173.
Springer, 2017.

[2] James Munkres. Topology. Pearson Education, 2014.

