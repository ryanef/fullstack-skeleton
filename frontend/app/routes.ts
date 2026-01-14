import type { RouteConfig } from "@react-router/dev/routes";
import { route } from "@react-router/dev/routes";

export default [
  route("dashboard", "routes/dashboard.tsx"),
] satisfies RouteConfig;