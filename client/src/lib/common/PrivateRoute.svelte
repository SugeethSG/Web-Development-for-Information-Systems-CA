<script>
  import user from "../../store/user";
  import { navigate } from "svelte-navigator";
  export let Component;

  if (!$user.isAuthenticated) navigate("/login", { replace: true });
</script>

<svelte:component this={Component} />
